import random
import re

from core.scripts.twitter_related import on_demand

from core.utils.logging import log
from scripts.twitter_related.random_poem.models import MinisherPoemSite


class GetRandomPoem(on_demand.BaseOnTimelineDemandScript):
    command_pattern = ''

    def received_command(self, command, data):
        match = re.search(self.command_pattern, command)

        if match:
            log("Asked for a poem, by {0}".format(data['user']['screen_name']))

            poem = self.get_random_poem()
            self.twitter.reply_to(data, poem)

    def get_random_poem(self):
        sites_list = [MinisherPoemSite]
        x = random.randint(0, len(sites_list) - 1)
        return sites_list[x].get_poem(sites_list[x]().get_body_as_soup_object())


GetRandomPoem().get_random_poem()