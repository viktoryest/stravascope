class Challenge:
    @staticmethod
    def get_activities(some_json):
        activities = []
        for i in some_json['sections']:
            if i['title'] == 'Details & Eligibility':
                current_list = i['content']
                for j in current_list:
                    if j['key'] == 'qualifyingActivities':
                        current_list_2 = j['qualifyingActivities']
                        for p in current_list_2:
                            activities.append(p)
        final_activities = []
        for j in activities:
            obj_with_act = Activity(j)
            final_activities.append(obj_with_act)
        return final_activities

    def __init__(self, json_file):
        self.title = json_file['header']['name'].replace("&#39;", "'")
        self.date = json_file['summary']['calendar']['title'].replace('</strong>', '').replace('<strong>', '')
        self.activities = self.get_activities(json_file)


class Activity:
    def __init__(self, json):
        self.activityType = json['activityType']
        self.text = json['text']


class Images:
    def __init__(self, json):
        self.background = json['header']['coverImageUrl']
        self.logo = json['header']['challengeLogoUrl']
