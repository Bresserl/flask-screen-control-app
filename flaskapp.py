from app import app, db
from app.models import File, Video, Text, Person


if __name__ == '__main__':
    app.run(debug=True)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Person': Person,
            'File': File, 'Text': Text, 'Video': Video}
