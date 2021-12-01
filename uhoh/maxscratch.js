async perspectify (image, {topLeft, topRight, bottmLeft, bottomRight, canvas = null}) {
    if(image.constructor.name !== 'Sharp')
      image = sharp(await this.toBuffer(image));
    
    const metadata = await image.metadata();
    const imgWidth = metadata.width;
    const imgHeight = metadata.height;
    
    if(canvas)
      image = image.flatten(canvas.color || 'transparent')
        .extend({
          top: 0,
          left: 0,
          bottom: canvas.height - imgHeight <= 0 ? 0 : canvas.height - imgHeight,
          right: canvas.width - imgWidth <= 0 ? 0 : canvas.width - imgWidth,
          background: canvas.color || 'transparent',
        });
    const imImage = im(await this.toBuffer(image));
    imImage.command('convert');
    imImage.out('-matte').out('-virtual-pixel').out('transparent').out('-distort').out('Perspective');
    imImage.out([
      [topLeft, 0, 0],
      [topRight, imgWidth, 0],
      [bottomLeft, 0, imgHeight],
      [bottomRight, imgWidth, imgHeight],
    ].map(point => `${point[1]},${point[2]},${point[0].x},${point[0].y}`).join(' '));
    return await this.imBuffer(imImage);
    
    const maxpic = await sharp(await this.toBuffer())
      .resize(110, 110, { fit: 'cover' })
      .toBuffer();
    const metadata = await sharp(this.resource('respects.png')).metadata();
    const perspective = await this.perspectify(avatar, {
      topLeft: { x: 366, y: 91 },
      topRight: { x: 432, y: 91 },
      bottomLeft: { x: 378, y: 196 },
      bottomRight: { x: 439, y: 191 },
      canvas: {
        width: metadata.width,
        height: metadata.height,
        color: '#ddd',
      },
    });
    const canvas = sharp(this.resource('respects.png'))
      .composite([
        { input: perspective, left: 0, top: 0, blend: 'dest-over' },
      ]);

    return this.send(message, canvas);
}