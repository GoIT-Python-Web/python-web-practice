from models import Post, User

if __name__ == '__main__':
    posts = Post.objects.all()

    print('------ Posts -------')
    for post in posts:
        print(post.to_mongo().to_dict())

    for post in Post.objects(tags='mongodb'):
        print(post.title)

    print('------ Users -------')
    users = User.objects.all()
    for user in users:
        print(user.to_mongo().to_dict())

    print('------ Others -------')
    posts = Post.objects(id="6499bf48e62c263b252e06e3").first()
    print(posts.to_mongo().to_dict())

    posts = Post.objects(title="Fun with MongoEngine").as_pymongo()
    print(posts)
