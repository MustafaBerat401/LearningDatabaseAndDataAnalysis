import pandas as pd
df = pd.read_csv("youtube-ing.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:].head()

# 3- Dataset'de bulunan kolon isimleri ve sayısını bulunuz.
result = df.info
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalann kolonları listeleyin
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed)
df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"], axis = 1, inplace = True)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalaması 
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6- İlk 50 videonun like ve dislike kolonlarını getiriniz.
result = df.head(50)[["title","likes","dislikes"]]

# 7- En çok görüntülenen video hangisidir?
# result = df[(df["views"].max()) == df["views"]][["title","views"]]

# 8- En düşük görüntülenen video hangisidir ?
result = df[df["views"].min() == df["views"]][["title","views"]]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?

result = df.sort_values("views",ascending=False)[["title","views"]].head(10)


# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
result = df.groupby("category_id").mean()["likes"].sort_values()

# 11- Kategoriye göre beğeni ortalamalarını sıralı bir şekilde getiriniz.
result = df.groupby("category_id").mean().sort_values("likes")["likes"]


# 12- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır?
# result = df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"] = df["title"].apply(len)
result = df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
# df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))


def tagCount(tag):
    return len(tag.split('|'))

df["tag_count"] = df["tags"].apply(tagCount)


# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)


def likesDislikesOraniHesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList)) 
    oranListesi = []
    for like,dislike in liste:
        if (like+dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"]=likesDislikesOraniHesapla(df)

print(df.sort_values("beğeni_orani",ascending=False)[["category_id","likes","dislikes","beğeni_orani"]])





