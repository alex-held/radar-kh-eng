import unittest
import translation

class TranslationTests(unittest.TestCase):

    def test_translate_ALARM(self):
        actual = translation.translate(message="🔴ТРЕВОГА\nБудет боевая работа по БПЛА\n\nУгроза по баллистике⚠️")
        self.assertEqual(actual,  second="🔴ALARM\nThere will be combat work on the UAV\n\nBallistics threat⚠️", msg=actual)

if __name__ == '__main__':
    unittest.main()