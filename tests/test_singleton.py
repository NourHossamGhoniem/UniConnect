from core.file_manager import FileManager

def test_file_manager_is_singleton():
    fm1 = FileManager()
    fm2 = FileManager()
    
    assert fm1 is fm2