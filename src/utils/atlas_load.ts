const convertToPixiAtlas: any = (originAtlasData: any) => {
  const atlasData: any = originAtlasData;
  atlasData.meta.scale = originAtlasData.meta.scale.toString();
  return atlasData;
};

export default convertToPixiAtlas;
