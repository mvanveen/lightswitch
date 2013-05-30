import os

from bottle import static_file
import bottle as app
import pystache

#from lightbulb.lightbulb import Lightbulb

#light = Lightbulb()

STATIC_PATH = os.path.abspath(
  os.path.join(os.path.abspath(__file__), '../../assets')
)
TEMPLATE_PATH = os.path.abspath(
  os.path.join(os.path.abspath(__file__),'../../views')
)

loader = pystache.loader.Loader(
  search_dirs=[TEMPLATE_PATH],
  extension='html',
  file_encoding='utf8'
)
renderer = pystache.renderer.Renderer(
  search_dirs=[TEMPLATE_PATH],
  file_extension='html',
  file_encoding='utf8'
)

@app.route('/assets/<path:path>')
def serve_static(path):
  return static_file(path, root=STATIC_PATH)


@app.route('/')
def handle_root():
  return renderer.render(loader.load_name('index'))


@app.route('/toggle')
def handle_toggle():
  state = light.toggle()
  return {
    'success': True,
    'on': state
  }

app.run(host='0.0.0.0')
