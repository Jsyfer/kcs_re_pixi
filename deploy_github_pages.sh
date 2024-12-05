git add kcs2/resources/ship/supply_character/0156_5734.png -f
git add kcs2/resources/ship/supply_character/0916_7140.png -f
git add kcs2/resources/ship/supply_character/0187_8548.png -f
git add kcs2/resources/ship/supply_character/0370_7203.png -f
git add kcs2/resources/ship/supply_character/0435_6959.png -f
git add kcs2/resources/ship/supply_character/0548_6235.png -f
git add kcs2/resources/ship/supply_character/0309_6502.png -f
git add kcs2/resources/ship/supply_character/0215_2734.png -f
git add kcs2/resources/ship/supply_character/0240_4907.png -f
git add kcs2/resources/ship/supply_character/0469_5061.png -f
git add kcs2/resources/ship/supply_character/0498_8052.png -f
git add kcs2/resources/ship/supply_character/0685_1465.png -f
git add kcs2/resources/ship/supply_character/0547_2576.png -f
git add kcs2/resources/ship/supply_character/0587_8200.png -f
git add kcs2/resources/ship/supply_character/0237_6815.png -f
git add kcs2/resources/ship/supply_character/0300_5716.png -f
git add kcs2/resources/ship/supply_character/0258_3875.png -f
git add kcs2/resources/ship/supply_character/0619_6331.png -f
git add kcs2/img/supply/supply_main.json -f
git add kcs2/img/supply/supply_main.png -f

git stash

git checkout gh-pages
git pull

git stash pop

git commit -a -m "add assets"
git push origin gh-pages

git checkout main