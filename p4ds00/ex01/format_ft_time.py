import time
import datetime

second_since_epoch = time.time()

formatted_seconds = "{:,.4f}".format(second_since_epoch)
scientific_notation = "{:.2e}".format(second_since_epoch)

current_date = datetime.date.today()

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(f"{current_date.strftime('%b %d %Y')}")