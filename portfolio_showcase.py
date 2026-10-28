"""
Akash V Technical Showcase CLI Explorer
Author: Akash V (@akashvenkey)
"""
def main():
    domains = {
        "Deep Learning": "Mathematical activations, NumPy continuous curves, AI ethics",
        "Business Analytics": "Power BI Superstore DAX dashboards, RFM segmentation, KPI metrics",
        "Full-Stack Web": "City Hospital portal, Netflix UI clone, responsive interfaces",
        "Data Warehousing": "Star schemas, multidimensional OLAP hypercubes, WEKA data mining"
    }
    print("==================================================")
    print("      AKASH V - SOFTWARE ENGINEERING PORTFOLIO    ")
    print("==================================================")
    for domain, summary in domains.items():
        print(f"• {domain:<20}: {summary}")
    print("GitHub: https://github.com/akashvenkey")

if __name__ == "__main__":
    main()