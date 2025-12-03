from io import BytesIO
import qrcode
from django.core.files.base import ContentFile
from django.db import models
from django.conf import settings
from events.models import Event

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tickets")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    quantity = models.PositiveIntegerField(default=1)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # ensure we have an ID
        # Generate a deterministic payload for validation/scanning
        payload = f"ticket_id:{self.id}|user_id:{self.user_id}|event_id:{self.event_id}|qty:{self.quantity}"
        img = qrcode.make(payload)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        filename = f"ticket_{self.id}.png"
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)
        super().save(update_fields=["qr_code"])
    
    def __str__(self):
        return f"{self.user} booked {self.quantity} for {self.event}"
