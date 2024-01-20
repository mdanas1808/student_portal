# students/tests.py
from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse
from unittest.mock import patch
from students.views import generate_qr_code

class QRCodeGenerationTest(TestCase):
    @patch('students.views.qrcode.QRCode.make_image')
    @patch('students.views.HttpResponse')
    def test_generate_qr_code(self, mock_http_response, mock_make_image):
        # Mock the QR code image and HttpResponse
        mock_image_instance = mock_make_image.return_value
        mock_http_response_instance = mock_http_response.return_value

        # Call the generate_qr_code function
        response = generate_qr_code(student_id=1)

        # Check that the response is an HttpResponse
        self.assertIsInstance(response, HttpResponse)

        # Check that the make_image method was called with the correct parameters
        mock_make_image.assert_called_once_with(fill_color='black', back_color='white')

        # Check the content attribute for the presence of image data
        content = response.content
        self.assertIn(b'\x89PNG', content)
        self.assertIn(b'IHDR', content)
        self.assertIn(b'IDAT', content)

        # You can add more assertions based on your specific requirements
        # For example, you could check the size of the image or other properties
