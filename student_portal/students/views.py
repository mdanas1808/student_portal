# students/views.py
from django.shortcuts import render
import csv
import qrcode
from django.http import HttpResponse
from django.conf import settings
from io import BytesIO

def read_student_data():
    student_data = []
    with open(settings.STUDENT_CSV_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_data.append(row)
    return student_data

def generate_qr_code(student_id):
    url = f'http://localhost:8000/student/{student_id}/'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # buffer = BytesIO()
    # img.save(buffer, format="PNG")

    # # Create an HTTP response object
    # response = HttpResponse(content_type='image/png')

    # # Set the content of the response to the captured image data
    # response.write(buffer.getvalue())

    buffer = HttpResponse(content_type='image/png')
    img.save(buffer, format="PNG")

    return buffer


    # response = HttpResponse(content_type="image/png")
    # response = HttpResponse()
    # img.save(response, "PNG")
    # response['content-type'] = 'image/png'
    # return response

def student_detail(request, student_id):
    student_data = read_student_data()
    student = next((s for s in student_data if s['id'] == student_id), None)
    if student:
        qr_code = generate_qr_code(student_id)
        # return render(request, 'students/student_detail.html', {'student': student})

        return render(request, 'students/student_detail.html', {'student': student, 'qr_code': qr_code})
    else:
        return render(request, 'students/student_not_found.html')

def index(request):
    student_data = read_student_data()
    return render(request, 'students/index.html', {'student_data': student_data})
