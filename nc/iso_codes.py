class Codes():
    def SPACE(self): return('')
    def FORMAT_FEEDRATE(self): return('%.2f') 
    def FORMAT_IN(self): return('%.5f')
    def FORMAT_MM(self): return('%.3f')
    def FORMAT_ANG(self): return('%.1f')
    def FORMAT_TIME(self): return('%.2f')
    def FORMAT_DWELL(self): return('P%f')

    def BLOCK(self): return('N%i' + self.SPACE())
    def COMMENT(self,comment): return( ('(%s)' % comment ) )
    def VARIABLE(self): return( '#%i')
    def VARIABLE_SET(self): return( '=%.3f')

    def PROGRAM(self): return( 'O%i')
    def PROGRAM_END(self): return( 'M02')

    def SUBPROG_CALL(self): return( 'M98' + self.SPACE() + 'P%i')
    def SUBPROG_END(self): return( 'M99')

    def STOP_OPTIONAL(self): return('M01')
    def STOP(self): return('M00')

    def IMPERIAL(self): return(self.SPACE() + 'G20')
    def METRIC(self): return(self.SPACE() + 'G21')
    def ABSOLUTE(self): return(self.SPACE() + 'G90')
    def INCREMENTAL(self): return(self.SPACE() + 'G91')
    def SET_TEMPORARY_COORDINATE_SYSTEM(self): return('G92' + self.SPACE())
    def REMOVE_TEMPORARY_COORDINATE_SYSTEM(self): return('G92.1' + self.SPACE())
    def POLAR_ON(self): return(self.SPACE() + 'G16')
    def POLAR_OFF(self): return(self.SPACE() + 'G15')
    def PLANE_XY(self): return(self.SPACE() + 'G17')
    def PLANE_XZ(self): return(self.SPACE() + 'G18')
    def PLANE_YZ(self): return(self.SPACE() + 'G19')

    def TOOL(self): return('T%i' + self.SPACE() + 'M06')
    def TOOL_DEFINITION(self): return('G10' + self.SPACE() + 'L1' + self.SPACE())

    def WORKPLANE(self): return('G%i')
    def WORKPLANE_BASE(self): return(53)

    def FEEDRATE(self): return(self.SPACE() + 'F')
    def SPINDLE(self, format, speed): return(self.SPACE() + 'S' + (format % speed))
    def SPINDLE_CW(self): return(self.SPACE() + 'M03')
    def SPINDLE_CCW(self): return(self.SPACE() + 'M04')
    def COOLANT_OFF(self): return(self.SPACE() + 'M09')
    def COOLANT_MIST(self): return(self.SPACE() + 'M07')
    def COOLANT_FLOOD(self): return(self.SPACE() + 'M08')
    def GEAR_OFF(self): return(self.SPACE() + '?')
    def GEAR(self): return('M%i')
    def GEAR_BASE(self): return(37)

    def RAPID(self): return('G00')
    def FEED(self): return('G01')
    def ARC_CW(self): return('G02')
    def ARC_CCW(self): return('G03')
    def DWELL(self): return('G04')
    def DRILL(self): return(self.SPACE() + 'G81')
    def DRILL_WITH_DWELL(self, format, dwell): return(self.SPACE() + 'G82' + (format % dwell))
    def PECK_DRILL(self): return(self.SPACE() + 'G83')
    def PECK_DEPTH(self, format, depth): return(self.SPACE() + 'Q' + (format % depth))
    def RETRACT(self, format, height): return(self.SPACE() + 'R' + (format % height))
    def END_CANNED_CYCLE(self): return(self.SPACE() + 'G80')

    def X(self): return(self.SPACE() + 'X')
    def Y(self): return(self.SPACE() + 'Y')
    def Z(self): return(self.SPACE() + 'Z')
    def A(self): return(self.SPACE() + 'A')
    def B(self): return(self.SPACE() + 'B')
    def C(self): return(self.SPACE() + 'C')
    def CENTRE_X(self): return(self.SPACE() + 'I')
    def CENTRE_Y(self): return(self.SPACE() + 'J')
    def CENTRE_Z(self): return(self.SPACE() + 'K')
    def RADIUS(self): return(self.SPACE() + 'R')
    def TIME(self): return(self.SPACE() + 'P')

    def PROBE_TOWARDS_WITH_SIGNAL(self): return('G38.2' + self.SPACE())
    def PROBE_TOWARDS_WITHOUT_SIGNAL(self): return('G38.3' + self.SPACE())
    def PROBE_AWAY_WITH_SIGNAL(self): return('G38.4' + self.SPACE())
    def PROBE_AWAY_WITHOUT_SIGNAL(self): return('G38.5' + self.SPACE())

    def MACHINE_COORDINATES(self): return('G53' + self.SPACE())

    def EXACT_PATH_MODE(self): return('G61' + self.SPACE())
    def EXACT_STOP_MODE(self): return('G61.1' + self.SPACE())
    def BEST_POSSIBLE_SPEED(self, motion_blending_tolerance, naive_cam_tolerance): 
	    statement = 'G64'

	    if (motion_blending_tolerance > 0):
		    statement += ' P ' + str(motion_blending_tolerance)

	    if (naive_cam_tolerance > 0):
		    statement += ' Q ' + str(naive_cam_tolerance)

	    return(statement + self.SPACE())

codes = Codes()
