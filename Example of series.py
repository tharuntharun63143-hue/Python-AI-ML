data = {
    "movie_name":["Mark","Devil","KGF","Landlord",45],
    "hero":["sudeep","Darashan","Yash","Duniya_vijya","shivanna"],
    "heroines":["priya","rachana_rai","srinidi_shetty","rachita_ram","sudharani"]
}
df = pd.DataFrame(data)
print("list of recent movies:\n",df)
print("\n list top movies:\n",df['movie_name'])

print("\n hero,heroines:",df['hero'],df["heroines"])
