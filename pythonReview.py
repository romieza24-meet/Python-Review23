
def create_youtube_video(title, description):
	yt_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return yt_video


def like(yt_video):
	# for key in yt_video:
	# 	if key == "likes":
	# 		print(key)
	# 		yt_video["likes"] += 1
	# 		return yt_video
	# 	else:
	# 		print(key)
	# 		return yt_video
		yt_video["likes"] += 1
		return yt_video


def dislike(yt_video):

		yt_video["dislikes"] += 1
		return yt_video


def add_comment(yt_video, username, comment_text):
	yt_video["comments"][username] = comment_text
	return yt_video

my_video = create_youtube_video("test_title", "test_description")

print(my_video)

like(my_video)
dislike(my_video)
add_comment(my_video, "test_user", "test comment")

print(my_video)

while my_video["likes"] < 495:
	my_video = like(my_video)
print(my_video)