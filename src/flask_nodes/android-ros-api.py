import os
from flask import Flask, send_file
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
print "Flask in the architecture: "
os.system("uname -m")

## Views
@app.route('/take_picture')
def take_picture():
    #front camera photo
    try:
        #os.system("am start -a android.media.action.IMAGE_CAPTURE")
        #os.system("input keyevent 27")
	#os.system("killall com.htc.camera")
	os.system("sh /storage/emulated/0/droid-server/src/android_nodes/take_picture.sh")
	return "ok view flask_nodes static folder", 201
    except AttributeError, e:
	print e
	return "error", 500    

@app.route('/take_video')
def take_video():
    #record 30 seconds video
    try:
        #os.system("am start -a android.media.action.VIDEO_CAPTURE")
	#os.system("input keyevent 27")
	#os.system("sleep 30s")
        #os.system("input keyevent 27")
	#os.system("killall com.htc.camera")
	os.system("sh /storage/emulated/0/droid-server/src/android_nodes/take_video.sh")
	return "ok view DCIM 100MEDIA folder", 201
    except AttributeError, e:
	print e
	return "error", 500    

@app.route('/take_audio')
def take_screenshot():
    try:
        os.system('screencap -p screen_$(date +"%F%T.png')
	return "ok", 201
    except AttributeError, e:
	print e
	return "error", 500    

@app.route('/broadcast')  
def camera():
    import androidhelper
    droid = androidhelper.Android()
    pic = "/storage/emulated/0/streamming.jpg"
    droid.cameraCapturePicture(pic)
    return send_file(pic, mimetype='image/jpeg')

#RESTful api
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')



if __name__ == '__main__':
    app.run(debug=True)


