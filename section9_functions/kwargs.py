def ensure_correct_info(**kwargs):
  return kwargs

print(ensure_correct_info(name="Caryssa", color="blue"))

def special_greeting(**kwargs):
  if "Caryssa" in kwargs and kwargs["Caryssa"] == "special":
    return "You get a special greeting"
  elif "Caryssa" in kwargs:
    return f"{kwargs['Caryssa']} Caryssa!"
  return "Not sure who this is"

print(special_greeting(Caryssa="special"))
print(special_greeting(Caryssa="Yo"))