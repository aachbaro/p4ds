ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[-1] = 'World!'
# Les liste sont mutable, je peux donc modifier un seul element a la fois

ft_tuple = ("Hello", "France!")
# contrairement au liste, je ne peux pas modifier les tuple apres leurs creation, je dois donc le recreer entierement

ft_set.remove("tutu!")
ft_set.add("Paris!")
# les ensemble sont mutable mais desordonne, je dois donc acceder a la valeur a modifier par sa valeur et non par son index

ft_dict["Hello"] = "42Paris!"
# Les dictionnaire fonctionnent par cles/valeurs, je peux donc acceder au valeurs via le noms de la cles

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
