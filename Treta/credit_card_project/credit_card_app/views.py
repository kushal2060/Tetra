from django.shortcuts import render
from django.http import JsonResponse
from .models import UserCreditCard
from .forms import UserCreditCardForm
from cryptography.fernet import Fernet
import json


from .encryption_utils import encrypt_credit_card, decrypt_credit_card

# Replace 'your_secret_key' with a secure key

def index(request):
    form = UserCreditCardForm()
    return render(request, 'index.html', {'form':form})










def store_credit_card(request):
    print("Reached store_credit_card view")  # Add this line for debugging
    if request.method == 'POST':
        print('All POST data:', request.POST) 
        form = UserCreditCardForm(request.POST)
        if form.is_valid():
            credit_card_info = form.save(commit=False)
            credit_card_info.encrypted_credit_card = encrypt_credit_card(form.cleaned_data['encrypted_credit_card'])
            credit_card_info.save()
            return JsonResponse({'message': 'Credit card information stored successfully'})
        else:
            print(form.errors.as_json())
            return JsonResponse({'error': 'Form validation failed'})

    return JsonResponse({'error': 'Invalid request method'})



def retrieve_credit_card(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            retrieval_email = json_data.get('email')

            # Retrieve encrypted credit card from the database using the email
            encrypted_credit_card = get_encrypted_credit_card(retrieval_email)

            if not encrypted_credit_card:
                return JsonResponse({'error': 'Error retrieving credit card information: Email not found in the database'})

            # Decrypt the credit card
            decrypted_credit_card = decrypt_credit_card(encrypted_credit_card)

            if 'error' in decrypted_credit_card:
                return JsonResponse({'error': f'Error during decryption: {decrypted_credit_card["error"]}'})
            
            # Convert bytes to base64-encoded string for JSON serialization
            decrypted_credit_card_str = decrypted_credit_card['data'].decode('utf-8')

            print('Decrypted Credit Card:', decrypted_credit_card_str)

            return JsonResponse({'credit_card': decrypted_credit_card_str})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format in the request body'})
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'})
    else:
        return JsonResponse({'error': 'Invalid request method'})




def get_encrypted_credit_card(email):
    print("Queried email:", email)
    print("All emails in the database:", UserCreditCard.objects.values_list('email', flat=True))

    try:
        print("Checking for email:", email)
        # Query the database for the encrypted credit card information based on the email
        credit_card_info_queryset = UserCreditCard.objects.filter(email__iexact=email)

        if credit_card_info_queryset.exists():
            # If the queryset is not empty, retrieve the first object
            credit_card_info = credit_card_info_queryset.first()
            print("Email found. Returning encrypted credit card.")
            return credit_card_info.encrypted_credit_card
        else:
            # Handle the case where the email is not found in the database
            raise ValueError('Email not found in the database')

    except Exception as e:
        # Handle other exceptions (e.g., database connection issues)
        raise ValueError(f'Error retrieving credit card information: {str(e)}')


