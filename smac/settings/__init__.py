from smac.settings.default import SETTINGS


class Settings:
    def __init__(self, settings: dict = {}):
        self._parsed = Settings._parse(settings)
    
    @staticmethod
    def _parse(user_settings, system_settings=SETTINGS):
        final_settings = {}
        for k, v in system_settings.items():
            print("---")
            print(v)
            
            # Call select_options recursively
            if isinstance(v, dict):
                t = {}
                if k in user_settings:
                    t = user_settings[k]

                final_settings[k] = Settings._parse(t, v)
            
            # Perform selection
            elif isinstance(v, list):
                selected_option = None
                for option in v:
                    # The key must always be present
                    if k not in option:
                        raise ValueError(f"Key {k} was not found in option {option}.")
                    
                    # Select the setting provided by user
                    if k in user_settings:
                        if user_settings[k] == option[k]:
                            selected_option = option
                            break
                    # Use default if not
                    else:
                        if option.get("_default", True):
                            selected_option = option
                            break
                        
                # Select default
                if selected_option is None:
                    selected_option = v[0]
                        
                # Now take the keys and overwrite the old ones
                for k2, v2 in selected_option.items():
                    final_settings[k2] = v2
                
                # Overwrite with user settings
                for k2, v2 in user_settings.items():
                    if k2 not in option:
                        raise ValueError(f"Key {k2} was not found in option {option}.")
                        
                    final_settings[k2] = v2

            else:
                print("YES")
                final_settings[k] = v
                
        return final_settings

    def _instantiate(self):
        pass
        
    def __repr__(self):
        string = "Settings:\n"
        for k, v in self._parsed.items():
            
            if isinstance(v, dict):
                string += f"-- {k}\n"
                for k2, v2 in v.items():
                    if k2[0] == "_":
                        continue
                    string += f"------ {k2}: {v2}\n"
            else:
                string += f"-- {k}: {v}\n"
                
        return string