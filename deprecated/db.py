"""
    DockerCI: Build System
    Author: Aaditya M Nair
    Created On: Tue Dec  8 11:14:04 IST 2015

    Abstracts all interactions with Database.
"""

import pymongo
conn = pymongo.MongoClient()
db = conn['dci']
log = db['logs']

def new_commit(loc, sha1, msg):
    """
    Adds new commit to database.
    """
    data = {
            'project':loc,
            'hash':sha1,
            'message':msg,
            }
    log.insert_one(data)

def add_status(sha1, status):
    """
    Updates build status of the commit.
    TODO: Error Handling
    """
    build = log.find_one({'hash':sha1})
    build['status'] = status
    log.update({'_id':build['_id']}, {'$set':build}, upsert=False)

def find_build(allbuilds = False):
    """
    Gets the status of the Last build.
    """
    build_list = []

    for build in log.find():
        build.setdefault('status', 'Building')
        build_list.append(build)

        if not allbuilds:
            break
    return build_list
