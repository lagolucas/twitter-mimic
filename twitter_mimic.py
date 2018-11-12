import get_tweets, verify_deletion

arrobas = [""]

print("Colentado novos tweets...")
get_tweets.get_all(arrobas)
print("Checando se tweets foram removidos...")
verify_deletion.verify(arrobas)