from flask_restful import Resource, reqparse

exemple_route_get_args = reqparse.RequestParser()
exemple_route_get_args.add_argument("user",type=str,required=True)
exemple_route_post_args = reqparse.RequestParser()
exemple_route_post_args.add_argument("user",type=str,required=True)
exemple_route_post_args.add_argument("password",type=str,required=True)
exemple_route_put_args = reqparse.RequestParser()
exemple_route_put_args.add_argument("user",type=str,required=True)
exemple_route_put_args.add_argument("password",type=str,required=True)
exemple_route_delete_args = reqparse.RequestParser()
exemple_route_delete_args.add_argument("user",type=str,required=True)

donnees = []

class exemple_route(Resource):
	def get(self): #récupérer le mot de passe d'un utilisateur
		body = exemple_route_get_args.parse_args()
		[user] = [body[i] for i in body]

		global donnees
		
		indexe = -1
		for i in range(len(donnees)):
			if donnees[i]["user"] == user:
				indexe = i

		#Je vérifie que l'utilisateur exite
		if indexe == -1:
			return {"retour":"L'utilisateur n'exite pas."}


		return {"retour":"ok","valeur":donnees[i]["password"]}

	def post(self): #ajouter un utilisateur
		body = exemple_route_post_args.parse_args()
		[user,password] = [body[i] for i in body]

		global donnees

		#Je vérifie que l'utilisateur n'existe pas déjà
		if any([1 for i in donnees if i["user"] == user]):
			return {"retour":"L'utilisateur existe déjà."}

		#J'ajoute l'utilisateur
		donnees += [{"user":user,"password":password}]

		return {"retour":"ok"}

	def put(self): #modifier le mot de passe d'un utilisateur
		body = exemple_route_put_args.parse_args()
		[user,password] = [body[i] for i in body]

		global donnees
		
		indexe = -1
		for i in range(len(donnees)):
			if donnees[i]["user"] == user:
				indexe = i

		#Je vérifie que l'utilisateur exite
		if indexe == -1:
			return {"retour":"L'utilisateur n'exite pas."}

		#Je modifie le mot de passe de l'utilisateur
		donnees[i]["password"] = password
			
		return {"retour":"ok"}

	def delete(self): #supprimer_un_match
		body = exemple_route_delete_args.parse_args()
		[user] = [body[i] for i in body]

		global donnees
		
		indexe = -1
		for i in range(len(donnees)):
			if donnees[i]["user"] == user:
				indexe = i

		#Si l'utilisateur n'existait pas déjà
		if indexe == -1:
			return {"retour":"ok","note":"L'utilisateur n'existait pas."}

		#Je supprimer l'utilisateur
		donnees.pop(indexe)

		return {"retour":"ok"}

class exemple_route_all(Resource):
	def get(self):
		global donnees
		return {"retour":"ok","valeur":donnees}
