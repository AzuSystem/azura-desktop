use cxx_qt_lib::{QGuiApplication, QQmlApplicationEngine, QUrl};
use std::path::Path;
use std::*;

mod backend;

fn main() {
    let mut app = QGuiApplication::new();
    let mut engine = QQmlApplicationEngine::new();

    let tmpdir = Path::new("/tmp/azura-desktop-area-icon-previews");

    // if not os.path.exists("/tmp/azura-desktop-area-icon-previews"):

    if !tmpdir.is_dir() {
        println!("`/tmp/azura-desktop-area-icon-previews` Created ( Required for Icon Previews )");
        fs::create_dir(tmpdir).unwrap();
    };

    if let Some(engine) = engine.as_mut() {
        engine.load(&QUrl::from("qrc:/layouts/Desktop.qml"));
    }

    if let Some(app) = app.as_mut() {
        app.exec();
    }
}