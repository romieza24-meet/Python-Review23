
def create_youtube_video(title, description, hashtag_value):
	yt_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtag": hashtag_value}
	return yt_video


def like(yt_video):
	if "dislikes" in yt_video:
		yt_video["likes"] += 1
		return yt_video


def dislike(yt_video):
		if "dislikes" in yt_video:
			yt_video["dislikes"] += 1
			return yt_video


def add_comment(yt_video, username, comment_text):
	yt_video["comments"][username] = comment_text
	return yt_video

def similarity_to_video(vid1, vid2):
	list1 = vid1["hashtag"]
	list2 = vid2["hashtag"]
	similarity = 0
	similar_item = 0
	for i in list1:
		for v in list2:
			if i == v:
				similar_item += 1
	len1 = len(list1)
	len2 = len(list2)
	if len1 > len2:
		similar_item = 100*(int(similar_item)/int(len1))
	else:
		similar_item = 100*(int(similar_item)/int(len2))
	return(similar_item)
vid1 = {"likes": 0, "dislikes": 0, "comments": {}, "hashtag": ['a', 'b', 'c', 'd']}
vid2 = {"likes": 0, "dislikes": 0, "comments": {}, "hashtag": ['a', 'b', '3']}
print(similarity_to_video(vid1, vid2))


my_video = create_youtube_video("test_title", "test_description", ["#test"])

print(my_video)

like(my_video)
dislike(my_video)
add_comment(my_video, "test_user", "test comment")

print(my_video)

while my_video["likes"] < 495:
	my_video = like(my_video)
print(my_video)