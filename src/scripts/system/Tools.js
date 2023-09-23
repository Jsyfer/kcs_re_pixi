export class Tools {
    static massiveRequire(req) {
        const files = {};

        req.keys().forEach(key => {
            files[key] = req(key)
        });

        return files;
    }
}
