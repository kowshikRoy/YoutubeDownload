from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from .models import Playlist,Video, Url
import youtube_dl,pafy
import subprocess,json

def index(request):
    return render(request, 'index.html')


def playlistInfo(request):
    if(request.GET['type'] == 'playlist' and request.GET['id'] != ''):
        data = {}
        url = "https://www.youtube.com/playlist?list=" + request.GET['id']
        video = pafy.get_playlist(url)
        data['playlist'] = str(video)

        videos = []
        for i in video['items']:
            videos.append(i['pafy'].videoid)
        data['videos'] = videos
        return JsonResponse(data)



def process(request):
    print(request)
    if(request.GET['type'] == 'video'):
        try:
            return render(request, 'video.html', {'video': pafy.new("https://www.youtube.com/watch?v="+ request.GET['id'])})
        except:
            return HttpResponse('<h3 style="color:red; text-align:center">Invalid Url</h3>')

        # return render(request , 'video.html', {'data': sanitize(retrieve(request.GET['id']))})
    elif (request.GET['type'] == 'playlist') :
        print("HI")


def haha(request):
    if(request.GET['type'] == 'video'):
        try:
            return render(request, 'newVideo.html', {'video': pafy.new("https://www.youtube.com/watch?v="+ request.GET['id'])})
        except:
            return HttpResponse('<h3 style="color:red; text-align:center">Invalid Url</h3>')

        # return render(request , 'video.html', {'data': sanitize(retrieve(request.GET['id']))})
    elif (request.GET['type'] == 'playlist') :
        print("HI")


        # try:
        #     plist = Playlist.objects.get(id=request.GET['id'])
        # except Playlist.DoesNotExist:
        #     plist = Playlist(id = request.GET['id'])
        #     url = "https://www.youtube.com/playlist?list=" + request.GET['id']
        #     info = subprocess.check_output(['youtube-dl','-j', url])
        #     info = info.decode('utf-8')
        #     v = loads(info)
        #     videos = []
        #     plist.save()
        #     for i in v:
        #         videos.append(Parse(i))
        #         if 'n_entries' in i : plist.ncounts = i['n_entries']
        #         if 'playlist_title' in i : plist.name = i['playlist_title']
            
        #     plist.save()

        # videos = [sanitize(x) for x in plist.video_set.all().order_by('playlist_index')]
        # return render(request, 'playlist.html', {'data': videos})


# def loads(s):
#     """A generator reading a sequence of JSON values from a string."""
#     while s:
#         s = s.strip()
#         obj, pos = json.JSONDecoder().raw_decode(s)
#         if not pos:
#             raise ValueError('no JSON object found at %i' % pos)
#         yield obj
#         s = s[pos:]

# def Parse(v):
#     video = Video()
#     video.id = v['id']
#     video.duration = v['duration']
#     video.fps  = v['fps']
    
#     video.thumbnail = v['thumbnail']
#     video.title = v['title']
#     if 'playlist_id' in v: video.playlist = Playlist.objects.get_or_create(id = v['playlist_id'])[0]
#     if 'playlist_index' in v : video.playlist_index = v['playlist_index']
#     video.save()
#     for i in v['formats']:
#         url = Url()
#         url.url = i['url']
#         url.ext = i['ext']
#         if i['vcodec'] != 'none': url.vcodec = 1
#         if i['acodec'] != 'none': url.acodec = 1
#         url.format_id = i['format_id']
#         if 'width' in i : url.width = i['width']
#         if 'height' in i : url.height = i['height']
#         url.video = video
#         if 'filesize' in i : url.size  = round(int(i['filesize'])/(1024. * 1024),1)
#         else: url.size = round(video.fps * video.duration * url.width * url.height / (1024 * 1024 ), 1)
#         url.save()
#     return video

# def retrieve(video_id):
#     try:
#         video = Video.objects.get(pk=video_id)
#         return video;
#     except Video.DoesNotExist:
#         video = None
    

#     url = "https://www.youtube.com/watch?v="+ video_id
#     info = subprocess.check_output(['youtube-dl','-j',url])
#     info = info.decode('utf-8')
#     v = json.loads(info)    
#     return Parse(v)

# def sanitize(video):
#     full = []
#     audio = []
#     for i in video.url_set.all():
#         if (i.vcodec and i.acodec): full.append(i)
#         elif i.acodec: audio.append(i)

#     context = {
#         'video' : video,
#         'full' : full,
#         'audio' : audio,
#     }
#     return context
