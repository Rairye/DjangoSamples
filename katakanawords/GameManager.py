from random import randint


questions = {"マンツーマン" : "one-on-one", "ピーマン" : "bell pepper", "クレーム" : "complaint", "サラリーマン" : "office worker", "アンケート" : "questionnaire",  "コント" : "skit", "アルバイト" : "part-time job", "カルテ" : "medical record",  "ワイシャツ" : "dress shirt", 
"コンセント" : "outlet", "マント" : "cloak", "レントゲン" : "x-ray", "カニング" : "cheating", "オートバイ" : "motorcycle", "ガソリンスタンド" : "gas station", "キャッチコピー" : "catch phrase", "カリウム" : "potassium", "ナトリウム" : "sodium", "ジェットコースター" : "roller coaster", 
"ジーパン" : "jeans", "テレビゲーム" : "video game", "マイブーム" : "my obsession", "マグカップ" : "mug", "ピエロ" : "clown", "さぼる" : "skip", "ウラン" : "uranium", "テーマ" : "theme", "ゼミ" : "seminar", "オフィスレディー" : "office worker",  "サービス" : "free of charge",  
"フリーサイズ" : "one size fits all",  "シャ—プペンシル" : "mechanical pencil", "キーホルダー" : "keychain", "キャッチボール" : "catch", "ズボン" : "pants", "ピンセット" : "tweezers",  "アフターサービス" : "after-sales service", "ガードマン" : "security guard", "ポテトフライ" : "French fries", 
"マイペース" : "my own pace", "タレント" : "entertainer", "チャック" : "zipper", "リフォーム" : "renovation", "ベビーカー" : "stroller", "ホチキス" : "stapler", "サイン" : "signature", "バーゲンセール" : "sale", }


class game():
	def __init__(self):
		self.current_question = 0
		self.game_questions = []
		numbers = set([])
		
		while len(numbers) < 5:
			numbers.add(randint(0,len(questions)-1))
		
		question_keys = list(questions.keys())
		
		for num in numbers:
			japanese = question_keys[num]
			english = questions[japanese]
			self.game_questions.append([japanese, english])

				
	def get_next_question(self):
		question = self.game_questions[self.current_question]
		self.current_question+=1
		return question