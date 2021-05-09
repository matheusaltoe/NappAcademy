from redes_sociais import PersonalSection, AlbumSection, PublicationSection, UploadCode
import pytest
import unittest

class TestSessoes:
    def test_class_personalsection(self):
        session = PersonalSection()
        assert isinstance(session, PersonalSection)

    def test_class_personalsection_msg(self):
        session = PersonalSection()
        msg = "Dados Pessoais"
        assert session.__repr__() == msg        

    def test_class_albumsection(self):
        session = AlbumSection()
        assert isinstance(session, AlbumSection)

    def test_class_albumsection_msg(self):
        session = AlbumSection()
        msg = "Sessão para fotos"
        assert session.__repr__() == msg        
    
    def test_class_publicationsection(self):
        session = PublicationSection()
        assert isinstance(session, PublicationSection)

    def test_class_publicationsection_msg(self):
        session = PublicationSection()
        msg = "Sessão publicações"
        assert session.__repr__() == msg       

    def test_class_uploadcode(self):
        session = UploadCode()
        assert isinstance(session, UploadCode)

    def test_class_uploadcode_msg(self):
        session = UploadCode()
        msg = "Sessão upload de código"
        assert session.__repr__() == msg

