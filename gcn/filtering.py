import gcn

# Define your custom handler here.
@gcn.include_notice_types(
    gcn.notice_types.FERMI_GBM_FLT_POS,  # Fermi GBM localization (flight)
    gcn.notice_types.FERMI_GBM_GND_POS,  # Fermi GBM localization (ground)
    gcn.notice_types.FERMI_GBM_FIN_POS)  # Fermi GBM localization (final)
def handler(payload, root):
    # Look up right ascension, declination, and error radius fields.
    pos2d = root.find('.//{*}Position2D')
    ra = float(pos2d.find('.//{*}C1').text)
    dec = float(pos2d.find('.//{*}C2').text)
    radius = float(pos2d.find('.//{*}Error2Radius').text)

    # Print.
    print('ra = {:g}, dec={:g}, radius={:g}'.format(ra, dec, radius))

# Listen for VOEvents until killed with Control-C.
gcn.listen(handler=handler)