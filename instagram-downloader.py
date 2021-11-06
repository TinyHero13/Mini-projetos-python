import instaloader, sys, os, re

url = input("Informe a URL: \n")
    
downloadDir = 'downloads'
os.chdir(downloadDir)

loader = instaloader.Instaloader(
  download_pictures=True,
  download_videos=True,
  filename_pattern='{profile}_{mediaid}'
)

expr = r'\/p\/([^\/]*)/'
found = re.search(expr,url)

if found:
    print("Baixando {}...".format(found.group(1)))
    post = instaloader.Post.from_shortcode(loader.context,found.group(1))
    loader.download_post(post,".")