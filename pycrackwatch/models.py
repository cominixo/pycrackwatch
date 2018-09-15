from datetime import datetime


# Base model class for the Crack and Game classes
class Model:
    def __init__(self, dict_data):
        self._dict = dict_data

    def get(self, name):
        try:
            value = self._dict[name]
            return value
        except Exception as e:
            raise e

    # Formats string to a datetime object
    def formatDate(self, date_string):
        date = datetime.strptime(date_string[5:-6], '%d %b %Y %H:%M:%S')
        return date

    def formatBool(self, boolstr):
        return True if boolstr == "true" else False


class Crack(Model):
    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return "<Crack - {}>".format(self.title)

    @property
    def title(self): return self.get('title')

    @property
    def scene_group(self): return self.get('sceneGroup')

    @property
    def date(self): return self.formatDate(self.get('date'))

    @property
    def image(self): return self.get('image')


class Game(Model):
    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return '<Game - {}>'.format(self.title)

    @property
    def title(self): return self.get('title')

    @property
    def link(self): return self.get('link')

    @property
    def pub_date(self): return self.formatDate(self.get('pubDate'))

    @property
    def images(self):
        image = self.get('image')
        image_cover = self.get('imageCover')
        image_poster = self.get('imagePoster')
        return (image, image_cover, image_poster)

    @property
    def crack_date(self): return self.formatDate(self.get('crackDate'))

    @property
    def is_AAA(self): return self.formatBool(self.get('isAAA'))

    @property
    def is_hot(self): return self.formatBool(self.get('isHot'))

    @property
    def NFOs_count(self): return int(self.get('NFOsCount'))

    @property
    def comments_count(self): return int(self.get('commentsCount'))

    @property
    def ratings(self): return int(self.get('ratings'))

    @property
    def followers_count(self): return int(self.get('followersCount'))

    @property
    def original_price(self): return float(self.get('OriginalPrice'))

    @property
    def best_prices(self):
        best_price1 = self.get('BestPrice1')
        best_price2 = self.get('BestPrice2')
        best_price3 = self.get('BestPrice3')
        return (best_price1, best_price2, best_price3)

    @property
    def original_platform(self): return self.get('OriginalPlatform')

    @property
    def best_platforms(self):
        best_platform1 = self.get('BestPlatform1')
        best_platform2 = self.get('BestPlatform2')
        best_platform3 = self.get('BestPlatform3')
        return (best_platform1, best_platform2, best_platform3)

    @property
    def DRMs(self):
        DRM1 = self.get('DRM1')
        DRM2 = self.get('DRM2')
        return (DRM1, DRM2)

    @property
    def scene_groups(self):
        scene_group1 = self.get('SceneGroup1')
        scene_group2 = self.get('SceneGroup2')
        return (scene_group1, scene_group2)

    @property
    def steam(self): return self.get('Steam')

    @property
    def origin(self): return self.get('Origin')

    @property
    def IMDB(self): return self.get('IMDB')

    @property
    def updated_at(self): return self.formatDate(self.get('updatedAt'))
