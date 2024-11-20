git add kcs2/resources/ship/banner/0156_6999.png -f
git add kcs2/resources/ship/banner/0916_2878.png -f
git add kcs2/resources/ship/banner/0187_7429.png -f
git add kcs2/resources/ship/banner/0309_1313.png -f
git add kcs2/resources/ship/banner/0370_6464.png -f
git add kcs2/resources/ship/banner/0435_9511.png -f
git add kcs2/resources/ship/banner/0548_4384.png -f
git add kcs2/resources/ship/banner/0685_2622.png -f
git add kcs2/resources/ship/banner/0215_3373.png -f
git add kcs2/resources/ship/banner/0240_9083.png -f
git add kcs2/resources/ship/banner/0469_1964.png -f
git add kcs2/resources/ship/banner/0498_2469.png -f
git add kcs2/resources/ship/banner/0619_6945.png -f
git add kcs2/resources/ship/banner/0547_9622.png -f
git add kcs2/resources/ship/banner/0587_8659.png -f
git add kcs2/resources/ship/banner/0237_8264.png -f
git add kcs2/resources/ship/banner/0300_7776.png -f
git add kcs2/resources/ship/banner/0258_2671.png -f

git stash

git checkout gh-pages
git pull

git stash pop

git commit -a -m "add assets"
git push origin gh-pages

git checkout main