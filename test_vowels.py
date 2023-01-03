import main

def test_vowels():
    assert main.vowel_captilization("") == ""
    assert main.vowel_captilization("a") == "A"
    assert main.vowel_captilization("A") == "A"
    assert main.vowel_captilization("b") == "b"
    assert main.vowel_captilization("B") == "b"
    assert main.vowel_captilization("aeiou") == "AEIOU"
    assert main.vowel_captilization("AEIOU") == "AEIOU"
    assert main.vowel_captilization("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert main.vowel_captilization("BCDFGHJKLMNPQRSTVWXYZ") == "bcdfghjklmnpqrstvwxyz"
    assert main.vowel_captilization("abc123!") == "Abc123!"
    assert main.vowel_captilization("ABC123!") == "Abc123!"
    assert main.vowel_captilization("Hello World") == "hEllO wOrld"
    assert main.vowel_captilization("This is a test") == "thIs Is A tEst"
    assert main.vowel_captilization("The quick brown fox jumps over the lazy dog") == "thE qUIck brOwn fOx jUmps OvEr thE lAzy dOg"