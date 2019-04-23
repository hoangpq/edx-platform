"""
Unit tests for ProgramEnrollment views.
"""
from __future__ import unicode_literals

from uuid import uuid4

from django.urls import reverse
from rest_framework.test import APITestCase

from lms.djangoapps.program_enrollments.models import ProgramEnrollment


class ProgramEnrollmentViewTests(APITestCase):
    """
    Tests for the ProgramEnrollment view.
    """

    def test_post(self):
        self.url = reverse('programs_api:v1:program_enrollments', args=[uuid4()])
        response = self.client.post(self.url, {
            'external_user_key': 'abc',
            'status': 'pending',
            'curriculum_uuid': uuid4()
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.read()['external_user_key'], 'abc')
