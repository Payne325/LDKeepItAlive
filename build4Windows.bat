echo "Removing old Build"
echo y | rmdir -r build
echo y | rmdir -r dist
rm keepalive.spec

echo "Begin Build"
echo y | pyinstaller keepalive.py

echo d | xcopy "assets" "dist/keepalive/assets" /E
echo d | xcopy "engine" "dist/keepalive/engine" /E

echo "Build Complete!"