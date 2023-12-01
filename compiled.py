import seleniumbase



if __name__ == '__main__':
    with seleniumbase.SB(uc=True, wire=True, use_wire=True) as sb:
        sb.driver.get('https://wolfstream.tv')
        
    