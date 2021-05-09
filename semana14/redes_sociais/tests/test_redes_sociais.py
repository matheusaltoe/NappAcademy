from redes_sociais import facebook, linkedin, github, instagram
from sessoes import PersonalSection, AlbumSection, PublicationSection, UploadCode
import pytest
import unittest

class TestRedesSociais:
    def test_class_facebook_instance(self):
        rede = facebook()
        assert isinstance(rede, facebook)

    def test_class_linkedin_instance(self):
        rede = linkedin()
        assert isinstance(rede, linkedin)
    
    def test_class_github_instance(self):
        rede = github()
        assert isinstance(rede, github)

    def test_class_instagram_instance(self):
        rede = instagram()
        assert isinstance(rede, instagram)