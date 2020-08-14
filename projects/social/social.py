import random


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'User({repr(self.name)})'

class SocialGraph:
    def __init__(self):
        self.reset()

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}


    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        
        for user_id in self.users:
            for friend_id in range(user_id +  1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])

        # def populate_graph_2(self, num_users, avg_friendships):
        #     #reset Graph 
        #     self.reset()

        #     # add users 
        #     for i in range(num_users):
        #         self.add_user(f"user{i}")

        #     target_friendships = num_users * avg_friendships
        #     total_friendships = 0

        #     collisions = 0

        #     while total_friendships < target_friendships:
        #         user_id = random.randint(1, self.last_id)
        #         friend_id = random.randint(1, self.last_id)

        #         if self.add_friendship(user_id, friend_id):
        #             total_friendships += 2 
        #         else: 
        #             collisions += 1

        #         print(f"collosions: {collisions}")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        
        # find all friends of a user ( friends of friends, etc...)

        # find all friends of a user 
        # for each friend, find all friends for that friend 
        # traverse through the network 
        # repeat until no more friends in the network :( 
        # if a friend is already visited, ignore them 
        # return the shortest path of friendship between them

        q = Queue()


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 2)
    print(sg.users)
    print()
    print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
