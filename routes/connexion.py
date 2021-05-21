from flask_restful import Api, Resource, reqparse



connexion1_post_args = reqparse.RequestParser()
connexion1_post_args.add_argument("user",type=str,required=True)
connexion1_post_args.add_argument("password",type=str,required=True)
connexion2_post_args = reqparse.RequestParser()
connexion2_post_args.add_argument("Nom",type=str,required=True)
connexion2_post_args.add_argument("Prenom",type=str,required=True)


class connexion1(Resource):
	def post(self): #s_inscrire
		body = connexion1_post_args.parse_args()
		[user,password] = [body[i] for i in body]

		users = {"Louise":"2304","Erwan":"3545"}

		if user in users:

			if users[user] == password:
				return "ok"
		return "pas ok"



class connexion2(Resource):
	def post(self): #verifier_son_adresse_mail
		body = connexion2_post_args.parse_args()
		[Nom,Prenom] = [body[i] for i in body]

		personnes = [{"Nom":"Kerbrat","Prenom":"Erwan","Age":24,"Partenaire":""},
					 {"Nom":"Leroux","Prenom":"Louise","Age":45,"Partenaire":"Auresh"}]

		for i in range(len(personnes)):
			if personnes[i]["Nom"]==Nom and personnes[i]["Prenom"]==Prenom:
				return personnes[i]["Partenaire"]	 

		return "none"


