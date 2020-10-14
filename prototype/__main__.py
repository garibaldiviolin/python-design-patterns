from .classes import Sheep


dolly = Sheep("Dolly")
dolly.sound()

dolly_clone = dolly.clone()
dolly.sound()
