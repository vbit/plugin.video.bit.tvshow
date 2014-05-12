
import util, urllib2
import xbmc

def playVideo(params):
    link = WEB_PAGE_BASE + params['link']
    response = urllib2.urlopen(link)
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, "source src='", "'")
        util.playMedia(params['title'], params['image'], videoLink, 'Video')
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))

def buildCategories():
    url = WEB_PAGE_BASE + '/the-loai/tvshow'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extractAll(content, 'idscroll="', '<ul class="thumn">')
        for link in links:
            params = {'makeCategories':1}
            params['link'] = util.extract(link,'href="','\"')
            params['title'] = util.extract(link,'/1">','</a>')
            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, 'DefaultVideo.png', 'DefaultVideo.png', True)

        util.endListing()
        xbmc.executebuiltin("Container.SetViewMode(502)")
        
        
    else:
        util.showError(ADDON_ID, 'Could not open URL CATEGORIES %s to create menu' %(url))

def buildShow(inputParams):
    url = WEB_PAGE_BASE + inputParams['link']
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extractAll(content, '<div class="col">', '</span>')
        for link in links:
            params = {'makeShows':1}           
            params['link'] = util.extract(link,'href="','\"')
            params['title'] = util.extract(link,'data-original-title="','\"')
            params['image'] = util.extract(link,'img src="','"')
            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, params['image'], params['image'], True)
        util.endListing()
        xbmc.executebuiltin("Container.SetViewMode(502)")

    else:
        util.showError(ADDON_ID, 'Could not open URL SHOW %s to create menu' %(url))

'''
def buildShow(inputParams):
	urls = util.extractLink(inputParams['link'])
	for x in range(1:40):
		url = WEB_PAGE_BASE + urls + x
		response = urllib2.urlopen(url)
		if response and response.getcode() == 200:
			content = response.read()
			links = util.extractAll(content, '<div class="col">', '</span>')
			for link in links:
				if 'tvshow' in inputParams['link']:
					params = {'makeShows':1}
				else:
					params = {'makeShows':1}
				params['title'] = util.extract(link,'data-original-title="','\"')
				params['link'] = util.extract(link,'href="','\"')
				params['image'] = util.extract(link,'img src="','"')
				link = util.makeLink(params)
				util.addMenuItem(params['title'], link, params['image'], params['image'], True)
			
			xbmc.executebuiltin("Container.SetViewMode(502)")

		else:
			util.endListing()
			util.showError(ADDON_ID, 'Could not open URL SHOW %s to create menu' %(url))
			break
'''
			
			
def buildPlay(inputParams):
    url = WEB_PAGE_BASE + inputParams['link']
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extract(content, 'a href="#">&laquo', 'href="#">&raquo')
        extractLinks = util.extractAll(links,'a href="','"')
        for link in extractLinks:
            params = {'makePlay':1}           
            params['link'] = link
            params['title'] = util.extractTitle(link)
            params['image'] = inputParams['image']

            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, params['image'], params['image'], False)
        util.endListing()
        xbmc.executebuiltin("Container.SetViewMode(502)")

        
    else:
        util.showError(ADDON_ID, 'Could not open URL PLAY %s to create menu' %(url))

WEB_PAGE_BASE = 'http://play.fpt.vn'
ADDON_ID = 'plugin.video.bit.tvshow'

parameters = util.parseParameters()

if 'makePlay' in parameters:
    playVideo(parameters)
elif 'makeShows' in parameters:
    buildPlay(parameters)
elif 'makeCategories' in parameters:
    buildShow(parameters)
else:
    buildCategories()




    



