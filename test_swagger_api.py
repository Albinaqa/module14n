import unittest
# подключа код, который написали
import swagger

'''
Swagger API  test v0.3
'''

# функция просто возвращает статус-код
def status(r):
    return r.status_code

# класс для апи тестов
class SwaggerAPITest(unittest.TestCase):
    def test_get_petinfo01(self):
        "Получение информации о питомце, позитивный"
        # сначала функция pet(1) выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet(1)), 200)
    def test_get_petinfo02(self):
        "Получение информации о питомце, негативный - не найден"
        self.assertEqual(status(swagger.pet(600)), 404)
    def test_get_petinfo03(self):
        "Получение информации о питомце, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet("2+2")), 400)
    # Тест обновлений питомца    
    def test_get_pet_upd01(self):
        "Обновление информации о питомце, позитивный"
        # сначала функция pet_upd(1,"dog") выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet_upd(1,"dog")), 200) 
    def test_get_pet_upd02(self):
        "Обновление информации о питомце, негативный"
        self.assertEqual(status(swagger.pet_upd(0,"cat")), 405) 
    def test_get_pet_upd03(self):
        "Обновление информации о питомце, Invalid ID"
        self.assertEqual(status(swagger.pet_upd("abc","frog")), 405) 
    def test_post_user_new01(self):
        "Добавление нового пользователя, позитивный"
        self.assertEqual(status(swagger.user_new(333, "Many", "Masha", "Sobakina", "many@mail.ru", "hgdfhg", "983455", 0)), 200)
    def test_post_user_new02(self):
        "Добавление нового пользователя, негативный"
        self.assertEqual(status(swagger.user_new(444, None, "Masha", "Sobakina", "many@mail.ru", "hgdfhg", "983455", 0)), 500)
    def test_post_user_new03(self):
        "Добавление нового пользователя, негативный"
        self.assertEqual(status(swagger.user_new("333a", "Lyly", "Masha", "Sobakina", "many@mail.ru", "hgdfhg", "983455", 0)), 500)
    def test_get_user01(self):
        "Получение информации о пользователе, позитивный"
        self.assertEqual(status(swagger.user("Many")), 200) 
    def test_get_user02(self):
        "Получение информации о пользователе, негативный"
        self.assertEqual(status(swagger.user(None)), 404) 
    def test_get_user03(self):
        "Получение информации о пользователе, негативный"
        self.assertEqual(status(swagger.user("Fedy555")), 404) 



if __name__ == '__main__':
    unittest.main(verbosity=2)