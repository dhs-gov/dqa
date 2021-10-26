# from docx import Document


def iterate_paragraphs(doc):
    for para in doc.paragraphs:
        print("Section style: ", para.style.name)
        if para.style.name.startswith('Heading'):
            print("HEADING! ", para.text)
        else:
            print(para.text)


def get_title(doc):
    for para in doc.paragraphs:
        if para.style.name.startswith('Title'):
            return para.text
    return None


def get_section(doc, heading_name):
    in_section = False
    paragraphs = []
    for para in doc.paragraphs:
        if para.style.name.startswith('Heading'):
            if in_section:
                #print("STOP - found new Heading", para.text)
                return paragraphs
            elif heading_name in para.text:
                print("Found Selected Section: ", para.text)
                in_section = True
        elif in_section:
            #print("Adding para: ", para.text)
            if para.text:
                paragraphs.append(para.text)
    return paragraphs


# ---------------------------------------------------------------------------


# file_path = '../use_cases_data/beverly_minor_data/APM-20-137_CPSS_Program_SELC-TP_Version_1.1_Update.docx'
# #file_path = '../use_cases_data/beverly_minor_data/WO28_NFIP_Pivot_SELC_Tailoring Plan_v1.0 (2020)_Final)_CTO_signed.docx'
# # file_path = '../use_cases_data/beverly_minor_data/sample_appvet_conops.docx'
#
# doc = Document(file_path)
# sections = doc.sections
# print("num sections: ", len(sections))
#
# # TEST
# iterate_paragraphs(doc)
# # -----------------------
#
# title = get_title(doc)
# print("Found Title: ", title)
# overview_paragraphs = get_overview_paragraphs(doc)
# for para in overview_paragraphs:
#     print("Overview para: ", para)
