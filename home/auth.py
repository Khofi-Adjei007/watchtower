import string
import csv

"""
Password Validation System by Khofi_adjei
This program validates a user password characters to make sure it meets accurate security
By convention:
a strong password must be at least 8 or more characters long
must be a combination of uppercases, special characters and numbers.
"""


class signup_password_validation:
    """ Initialize the class"""

    def __init__(self, user_password_input):
        self.user_password_input = user_password_input

    # Signup Password Validation method
    def password_validation(self):
        in_list_1 = False
        in_list_2 = False
        in_list_3 = False

    # Variables to retrieve and store characters to be checked for
        special_chars = string.punctuation
        num_chars = string.digits
        upercase_chars = string.ascii_uppercase

        if len(self.user_password_input) < 8:
            print(
                "\nRequirement Fail!\nCharacters Must Be At Least Eight (8) charcters long")

    # Loop to inspect and verify the characters
        for chars in self.user_password_input:
            if chars in special_chars:
                in_list_1 = True
            elif chars in num_chars:
                in_list_2 = True
            elif chars in upercase_chars:
                in_list_3 = True

        if in_list_1 and in_list_2 and in_list_3:
            print("Requirment Success!\n")
        else:
            print(
                "Password Must Contain At Least\nA special Charcter \nA Number \nAnd An UpperCase")


user_password_input = input("Enter your password: ")
Validation = signup_password_validation(user_password_input)
Validation.password_validation()


in_list_1 = False
in_list_2 = False
in_list_3 = False


def valiadtion():
    global in_list_1 
    global in_list_2 
    global in_list_3 

    special_chars = string.punctuation
    num_chars = string.digits
    upercase_chars = string.ascii_uppercase



def submissionpdf(request):
    if request.method == 'POST':
        text = request.POST.get('docket_forms', '')

        # Generate PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="submission_{datetime.now().strftime("%Y-%m-%d")}.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        styles = getSampleStyleSheet()
        style_normal = styles['Normal']

        content = []
        content.append(Paragraph("Form Content:", style_normal))
        content.append(Spacer(1, 12))
        content.append(Paragraph(text, style_normal))

        doc.build(content)
        
        return response

    else:
        return HttpResponse("This view only accepts POST requests.")
    

  # Check if passwords match
        if password != password_two:
            password_mismatch_error = 'Passwords do not match.'
            return render(request, 'practice_page.html', {'password_mismatch_error': password_mismatch_error})

        # Check password complexity requirements
        if not (any(char.isupper() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in string.punctuation for char in password)):
            password_complexity_error = 'Password must contain at least one special character, one digit, and one uppercase letter.'
            return render(request, 'practice_page.html', {'password_complexity_error': password_complexity_error})

        # Check if email or username already exists
        if User.objects.filter(email=email).exists():
            email_exists_error = 'This email has already been used.'
            return render(request, 'practice_page.html', {'email_exists_error': email_exists_error})
        
        elif User.objects.filter(username=username).exists():
            username_exists_error = 'Username already exists.'
            return render(request, 'practice_page.html', {'username_exists_error': username_exists_error})