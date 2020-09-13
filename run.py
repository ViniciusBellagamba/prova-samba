from models.medias import app, create_video_table


create_video_table()
app.run(debug=False, port=8080, host='0.0.0.0', use_reloader=False)


