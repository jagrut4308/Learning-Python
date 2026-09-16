#keys need not be strings
month={
    "Jan":"January","Feb":"February","Mar":"March",
    "Apr":"April","May":"May","Jun":"June","Jul":"July",
    "Aug":"August","Sep":"September","Oct":"October",
    "Nov":"November","Dec":"Decemeber"
}
print(month.get("Jan")) #gives wht maps to key, in this case Jan
print(month.get("Mon","Not a valid key"))#default value, if it does not map
