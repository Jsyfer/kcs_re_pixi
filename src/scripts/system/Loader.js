export class Loader {
    constructor(loader, config, container) {
        this.loader = loader;
        this.config = config;
        this.resources = {};
        this.container = container
    }

    preload() {
        for (const asset of this.config.loader) {
            let key = asset.key
            if (asset.key.indexOf(".png") !== -1 || asset.key.indexOf(".jpg") !== -1) {
                this.loader.add(key, asset.data.default)
            }
        }

        console.log(this.container)
        this.loader.onProgress.add((percent) => {

            this.container.scale.x = percent.progress/100;
            // console.log(this.container.width)

            // this.container.width = percent.progress * 965;
            // I NEED TO SHOW PRELOADING BAR PROGRESS IN HERE
        });
           

        return new Promise(resolve => {
            this.loader.load((loader, resources) => {
                this.resources = resources;
                resolve();
            });
        });
    }
}