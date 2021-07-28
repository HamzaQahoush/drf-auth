from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Players

# Create your tests here.
class PlayersTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username="test_user", password="pass"
        )
        test_user.save()

        test_player = Players.objects.create(
            author=test_user,
            player_Name="messi",
            position="attacker",
            age=31,
            team="Barcelona",
        )

        test_player.save()

    def test_player_content(self):
        player = Players.objects.get(id=1)
        actual_author = str(player.author)
        actual_player_Name = str(player.player_Name)
        actual_position = str(player.position)
        actual_age = int(player.age)
        actual_team = str(player.team)

        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_player_Name, "messi")
        self.assertEqual(actual_position, "attacker")
        self.assertEqual(actual_team, "Barcelona")
